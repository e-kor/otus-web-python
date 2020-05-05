import React, {Component} from 'react'
import axios from "axios";
import Tag from "../course-list/Tag";
import LessonListItem from "./LessonListItem";
import './CourseDetails.css'

const API_URL = '/api/courses/';

class CourseDetails extends Component {
    state = {
        id: 0,
        description: "",
        isActive: true,
        lessons: [],
        name: "",
        tags: [],
        tutorName: ""
    };

    fetchData = () => {
        axios.get(`${API_URL}${this.props.id}`)
            .then(response => {
                this.setState(response.data)
            });
    };

    componentDidMount() {
        this.fetchData()
    }

    render() {
        const courseData = this.state;
        return (
            <div className="course-details">
                <h2 className="course-details__name">{courseData.name}</h2>
                <div className="course-details__author">Автор: {courseData.tutorName}</div>
                <div className="course-details__description">Описание: {courseData.description}</div>
                <div className="course-details__tags">{courseData.tags.map((tagName, index) => (<Tag name={tagName}/>))}</div>
                <div className="course-details__lessons">
                    <h3 className="course-details__lessons__header">Занятия</h3>
                    {courseData.lessons.map(({id, date, name, description}, index) => (
                        <LessonListItem key={index} id={id} date={date} name={name} description={description}/>))}
                </div>
            </div>

        )
    }
}

export default CourseDetails;
