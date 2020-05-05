import React from 'react';
import './CourseListItem.css'
import Tag from "./Tag";

const CourseListItem = props => {
    const {id, name, description, tags, tutorName, isActive} = props

    return (
        <div className="course-list-item">
            <div className="course-list-item__name">{name}</div>
            <div className="course-list-item__description">{description}</div>
            {tags.map((tagName, index) => (
                <Tag name={tagName}/>))}
        </div>

    )
}

export default CourseListItem
