import axios from "axios";

const BASE_URL = '/api/';
const COURSES_URL = `${BASE_URL}courses/`;
const AUTH_URL = `${BASE_URL}auth/`;
const MISC_URL = `${BASE_URL}misc/`;

export default class APIService {
    fetchCourseList = (pageNumber) => {
        return axios.get(`${COURSES_URL}?page=${pageNumber}`)
    };

    fetchCourseDetails = (courseId) => {
        return axios.get(`${COURSES_URL}${courseId}`)
    };
    fetchMyCourseList = () => {
        return axios.get(`${COURSES_URL}my`)
    };

    joinCourse = (courseId) => {
        return axios.post(`${COURSES_URL}${courseId}/join/`, {})
    };

    leaveCourse = (courseId) => {
        return axios.post(`${COURSES_URL}${courseId}/leave/`, {})
    };
    login = ({username, password}) => {
        return axios.post(`${AUTH_URL}token-get/`, {username, password})
    };

    register = ({username, password}) => {
        return axios.post(`${AUTH_URL}register/`, {username, password})
    };

    sendFeedback = ({email, body}) => {
        return axios.post(`${MISC_URL}feedback/`, {email, body})
    };


}
