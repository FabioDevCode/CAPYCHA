from fastapi import APIRouter, HTTPException, Depends # type: ignore
from sqlmodel import select, Session # type: ignore

from app.models.project import Project
from app.models.project_schemas import ProjectCreate, ProjectRead, ProjectUpdate
from app.models import get_session

router = APIRouter()


@router.post("/", response_model=ProjectRead)
def create_project(data: ProjectCreate, session: Session = Depends(get_session)):
    project = Project(domain=data.domain)
    session.add(project)
    session.commit()
    session.refresh(project)
    return project

@router.get("/", response_model=list[ProjectRead])
def get_all_projects(session: Session = Depends(get_session)):
    projects = session.exec(select(Project)).all()
    return projects

@router.get("/{project_id}", response_model=ProjectRead)
def get_project(project_id: str, session: Session = Depends(get_session)):
    project = session.get(Project, project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project

@router.put("/{project_id}", response_model=ProjectRead)
def update_project(project_id: str, data: ProjectUpdate, session: Session = Depends(get_session)):
    project = session.get(Project, project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    if data.domain is not None:
        project.domain = data.domain

    session.add(project)
    session.commit()
    session.refresh(project)
    return project

@router.delete("/{project_id}")
def delete_project(project_id: str, session: Session = Depends(get_session)):
    project = session.get(Project, project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    session.delete(project)
    session.commit()
    return {"ok": True}
