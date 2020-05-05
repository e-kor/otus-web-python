import * as $ from 'jquery';
import axios from 'axios';

const API_URL = "/api/";


function renderCourses(coursesData) {
    coursesData.results.forEach(courseData => {
        $("#course-list").append(`<li>${courseData.name}</li>`);
    });
}

function main() {
    axios.get(`${API_URL}courses`)
        .then(response => {
            renderCourses(response.data);
        });
}

main();