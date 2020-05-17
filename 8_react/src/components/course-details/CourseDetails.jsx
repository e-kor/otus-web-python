import React, {Component} from 'react'
import Tag from "../course-list/Tag";
import LessonListItem from "./LessonListItem";
import './CourseDetails.css'
import APIService from "../APIservice";
import Button from "react-bootstrap/Button";


class CourseDetails extends Component {
    constructor(props) {
        super(props);
        this.state = {
            id: 0,
            description: "",
            isActive: true,
            lessons: [],
            name: "",
            tags: [],
            tutorName: "",
            joined: false
        };
        this.apiService = new APIService();
    }

    handleJoinChange = () => {
        if (this.state.joined) {
            return this.apiService.leaveCourse(this.state.id).then(() => {
                this.setState({joined: false})
            })
        } else {
            return this.apiService.joinCourse(this.state.id).then(() => {
                this.setState({joined: true})
            })
        }

    }


    fetchData = () => {
        this.apiService.fetchCourseDetails(this.props.id)
            .then(response => {
                this.setState(response.data)
            });
    };

    componentDidMount() {
        this.fetchData()
    }


    render() {
        const button = <Button className="course-details__join-button"
                               variant={this.state.joined ? "outline-danger" : "outline-primary"}
                               onClick={this.handleJoinChange}>{this.state.joined ? "Leave" : "Join"}</Button>
        const courseData = this.state;
        return (
            <div className="course-details">
                <h2 className="course-details__name">{courseData.name}</h2>
                <div className="course-details__author">Автор: {courseData.tutorName}</div>
                <div className="course-details__description">Описание: {courseData.description}</div>
                <div className="course-details__tags">{courseData.tags.map((tagName, index) => (
                    <Tag name={tagName}/>))}</div>
                {localStorage.token && button}
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
