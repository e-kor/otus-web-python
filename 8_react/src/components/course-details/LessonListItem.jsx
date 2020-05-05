import React from 'react';
import './LessonListItem.css'

const LessonListItem = props => {
    const {id, date, name, description} = props

    return (
        <div className="lesson-list-item">
            <div className="lesson-list-item__date">{date}</div>
            <div className="lesson-list-item__name">{name}</div>
            <div className="lesson-list-item__description">{description}</div>
        </div>

    )
}

export default LessonListItem
