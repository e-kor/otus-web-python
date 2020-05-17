import React, {Component} from 'react'
import './CourseList.css'
import APIService from "../APIservice";
import CourseList from "./CourseList";


class CourseListMy extends Component {
    constructor(props) {
        super(props);
        this.apiService = new APIService();
    }


    render() {
        return (
            <CourseList loadData={this.apiService.fetchMyCourseList} header={"My courses"}/>
        )
    }
}

export default CourseListMy
