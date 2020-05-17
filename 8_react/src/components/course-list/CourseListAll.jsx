import React, {Component} from 'react'
import './CourseList.css'
import APIService from "../APIservice";
import CourseList from "./CourseList";


class CourseListAll extends Component {
    constructor(props) {
        super(props);
        this.apiService = new APIService();
    }


    render() {
        return (
            <CourseList loadData={this.apiService.fetchCourseList} header={"All available courses"}/>
        )
    }
}

export default CourseListAll
