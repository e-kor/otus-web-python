import React, {Component} from 'react'
import InfiniteScroll from "react-infinite-scroll-component";
import CourseListItem from "./CourseListItem";
import './CourseList.css'
import APIService from "../APIservice";
import Loader from 'react-loader-spinner'


class CourseList extends Component {
    constructor(props) {
        super(props);
        this.state = {
            coursesData: [],
            nextPageNumber: 1,
            hasNext: true
        };
        this.apiService = new APIService();
    }


    componentDidMount() {
        this.fetchMoreData()
    }

    fetchMoreData = () => {
        this.apiService.fetchCourseList(this.state.nextPageNumber).then(response => {
            this.setState({
                coursesData: [...this.state.coursesData, ...response.data.results],
                nextPageNumber: response.data.nextPageNumber,
                hasNext: response.data.hasNext
            })
        });
    };

    render() {
        return (
            <div className="course-list">
                <h1 className="course-list__header">Courses</h1>
                <InfiniteScroll
                    className="course-list__items"
                    dataLength={this.state.coursesData.length}
                    next={this.fetchMoreData}
                    hasMore={this.state.hasNext}
                    loader={<Loader className="course-list__loader"
                        type="TailSpin"
                        color="grey"
                        height={100}
                        width={100}
                        timeout={3000} //3 secs

                    />}
                    height={800}
                >
                    {this.state.coursesData.map(({id, name, description, tags, tutorName, isActive}, index) => (
                        <CourseListItem id={id} name={name} description={description} key={id} tags={tags}
                                        tutorName={tutorName} isActive={isActive}/>))}
                </InfiniteScroll>
            </div>


        )
    }
}

export default CourseList
