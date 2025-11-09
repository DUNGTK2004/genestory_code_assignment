import schemas, models
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status, APIRouter, Response, Query
from sqlalchemy.exc import IntegrityError
from database import get_db
from ml.inference import predict_priority

router = APIRouter()

@router.get("/tasks", response_model=list[schemas.Task])
def get_tasks(db: Session = Depends(get_db), is_done: bool | None = Query(None)):
    query = db.query(models.Task)
    if is_done is not None:
        query = query.filter(models.Task.is_done == is_done)
    return query.all()


@router.get('/tasks/{taskId}', response_model=schemas.Task)
def get_tasks(taskId: int, db: Session = Depends(get_db)):
    task = db.query(models.Task).filter(models.Task.id == taskId).first()
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                           detail=f"No task with this id: {taskId} found")
    return task

@router.post('/tasks', response_model=schemas.TaskCreate, status_code=status.HTTP_201_CREATED)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    new_task = models.Task(
        title = task.title,
        description = task.description,
        priority = task.priority,
        is_done = task.is_done
    )

    db.add(new_task)

    try:
        db.commit()
        db.refresh(new_task)
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Task with this title already exists")

    return new_task

@router.put('/tasks/{taskId}', response_model=schemas.TaskUpdate)
def update_task(taskId: int, task: schemas.TaskUpdate, db: Session = Depends(get_db)):
    task_query = db.query(models.Task).filter(models.Task.id == taskId)
    db_task = task_query.first()

    if not db_task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f'No note with this id: {taskId} found')
    
    update_data = task.model_dump(exclude_unset=True)

    if 'title' in update_data:
        existing_title = db.query(models.Task).filter(
            models.Task.title == update_data['title'],
            models.Task.id != taskId
        ).first()
        if existing_title:
            raise HTTPException(status_code=400, detail="Another task with this title already exists.")
        
        task_query.update(update_data, synchronize_session=False)
        db.commit()
        db.refresh(db_task)
        return db_task

@router.delete('/tasks/{taskId}')
def delete_task(taskId: int, db: Session = Depends(get_db)):
    task_query = db.query(models.Task).filter(models.Task.id == taskId)
    task = task_query.first()

    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"No Task with this id: {taskId} found")

    task_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.post("/predict-priority/")
def predict_priority_api(req: schemas.PredictRequest, db: Session = Depends(get_db)):
    text = req.title + " " + (req.description or "")
    pred = predict_priority(db, text, task_id=1)
    return {"predicted_priority": pred}




    

