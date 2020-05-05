import React from 'react';
import './CourseListItem.css'

const CourseListItem = props => {
    const {id, name, description, tags, tutorName, isActive} = props

    return (
        <div className="course-list-item">
            <div className="course-list-item__name">{name}</div>
            <div className="course-list-item__description">{description}</div>
        </div>

    )
}

export default CourseListItem
