import axios from "axios";
import {useHistory} from "react-router-dom";

const BASE_URL = '/api/';
const COURSES_URL = `${BASE_URL}courses/`;
const AUTH_URL = `${BASE_URL}auth/`;
const MISC_URL = `${BASE_URL}misc/`;

export default class APIService {

    constructor() {
        this.api = axios.create({headers: {
            common: {
                Authorization: localStorage.token?`Bearer ${localStorage.token}`:null
            }
            }});
    }

    fetchCourseList = (pageNumber) => {
        return this.api.get(`${COURSES_URL}?page=${pageNumber}`)
    };

    fetchCourseDetails = (courseId) => {
        return this.api.get(`${COURSES_URL}${courseId}`)
    };
    fetchMyCourseList = () => {
        return this.api.get(`${COURSES_URL}my`)
    };

    joinCourse = (courseId) => {
        return this.api.post(`${COURSES_URL}${courseId}/join/`, {})
    };

    leaveCourse = (courseId) => {
        return this.api.post(`${COURSES_URL}${courseId}/leave/`, {})
    };
    login = ({username, password}) => {
        return this.api.post(`${AUTH_URL}token-get/`, {username, password})
            .then(response =>{
             const   data = response.data;
            localStorage.setItem("token", data.access);
            localStorage.setItem("refreshToken", data.refresh);
        });
    };

    register = ({username, password}) => {
        return this.api.post(`${AUTH_URL}register/`, {username, password})
    };

    sendFeedback = ({email, body}) => {
        return this.api.post(`${MISC_URL}feedback/`, {email, body})
    };


}
