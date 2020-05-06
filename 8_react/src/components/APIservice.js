import axios from "axios";

const BASE_URL = '/api/';
const COURSES_URL = `${BASE_URL}courses/`;

export default class APIService {
    fetchCourseList = (pageNumber) => {
        return axios.get(`${COURSES_URL}?page=${pageNumber}`)
    };

    fetchCourseDetails = (courseId) => {
        return axios.get(`${COURSES_URL}${courseId}`)
    };


}
