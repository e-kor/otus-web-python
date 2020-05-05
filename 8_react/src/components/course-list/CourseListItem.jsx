import React from 'react';
import './CourseListItem.css'
import Popup from "reactjs-popup";
import Tag from "./Tag";
import CourseDetails from "../course-details/CourseDetails";

const CourseListItem = props => {
    const {id, name, description, tags, tutorName, isActive} = props

    return (
        <div className="course-list-item">
            <Popup
                trigger={<div className="course-list-item__general">
                    <div className="course-list-item__name">{name}</div>
                    <div className="course-list-item__description">{description}</div>
                </div>}
                modal
                closeOnDocumentClick
            >
                <CourseDetails id={id}/>
            </Popup>
            {tags.map((tagName, index) => (<Tag name={tagName}/>))}
        </div>

    )
}

export default CourseListItem
