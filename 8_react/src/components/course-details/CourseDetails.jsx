import React, {Component} from 'react'
import './CourseDetails.css'
import axios from "axios";
import Tag from "../course-list/Tag";
import LessonListItem from "./LessonListItem";
const API_URL = '/api/courses/'
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
    }

    componentDidMount() {
        this.fetchData()
    }
    render(){
        const courseData = this.state;
        return (
            <div className="course-details">
                <h1 className="course-details__name">{courseData.name}</h1>
                <div className="course-details__author">Автор: {courseData.tutorName}</div>
                <div className="course-details__description">Описание: {courseData.description}</div>
                {courseData.tags.map((tagName, index) => (<Tag name={tagName}/>))}
                {courseData.lessons.map(({id, date, name, description}, index) => (<LessonListItem id={id} date={date} name={name} description={description}/>))}
            </div>

        )
    }
};

export default CourseDetails;