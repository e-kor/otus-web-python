import React, {Component} from 'react'
import InfiniteScroll from "react-infinite-scroll-component";
import axios from 'axios';
import CourseListItem from "./CourseListItem";
import './CourseList.css'

const API_URL = '/api/courses/';


class CourseList extends Component {
    initialState = {
        coursesData: [],
        nextPageNumber: 1,
        hasNext: true
    }

    state = this.initialState;

    componentDidMount() {
        this.fetchMoreData()
    }

    fetchMoreData = () => {
        console.log(this)
        axios.get(`${API_URL}?page=${this.state.nextPageNumber}`)
            .then(response => {
                this.setState({
                    coursesData: [...this.state.coursesData, ...response.data.results],
                    nextPageNumber: response.data.nextPageNumber,
                    hasNext: response.data.hasNext
                })
            });
    }

    render() {
        return (
            <div className="course-list">
                <div className="course-list__header">Courses</div>
                <InfiniteScroll
                    className="course-list__items"
                    dataLength={this.state.coursesData.length}
                    next={this.fetchMoreData}
                    hasMore={this.state.hasNext}
                    loader={<h4>Loading...</h4>}
                    height={600}
                >
                    {this.state.coursesData.map(({id, name, description, tags, tutorName, isActive}, index) => (
                        <CourseListItem id={id} name={name} description={description} key={id} tags={tags} tutorName={tutorName} isActive={isActive}/>))}
                </InfiniteScroll>
            </div>


        )
    }
}

export default CourseList
