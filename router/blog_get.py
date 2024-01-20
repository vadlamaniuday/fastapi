from enum import Enum
from typing import Optional

from fastapi import APIRouter, Response, status

router = APIRouter(prefix="/blog", tags=["blog"])


class BlogType(str, Enum):
    short = "short"
    story = "story"
    howto = "howto"


@router.get(
    "/all",
    summary="Gets all blogs",
    description="This api call gets all the blogs present in database ",
    response_description="Gives the list of all avaiable blogs",
)
def get_all_blogs(page=1, page_size=5):
    return {"message": f"All {page_size} blogs on page {page}"}


@router.get("/{id}/comments/{comment_id}", tags=["comment"])
def get_comments(
    id: int, comment_id: int, valid: bool = True, username: Optional[str] = None
):
    """
    Simulates retrieving the specific comment of a specific blog with the help of comment id for comment and blog id for blog

        - :param id: mandatory path parameter
        - :param comment_id: mandatory path parameter
        - :param valid: optional query parameter
        - :param username: optional query parameter
        - :return: returns everything
    """
    return {
        "message": f"Blog : {id} comment: {comment_id},valid : {valid} , username : {username}"
    }


@router.get("/type/{types}")
def get_blog_type(types: BlogType):
    return {"message": f"Blog type is {types.name}"}


@router.get("/{id}", status_code=status.HTTP_200_OK)
def get_blog(id: int, response: Response):
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"message": f"blog with id {id} not found"}
    else:
        response.status_code = status.HTTP_200_OK
        return {"message": f"Blog with id : {id}"}
