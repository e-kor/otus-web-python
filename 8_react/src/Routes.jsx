import React from 'react'
import {IndexRoute, Route, Router} from 'react-router'

import App from './App'
import Login from './components/Login'
import LoginView from "./components/auth-views/LoginView";
import SignupView from "./components/auth-views/SignUpView";
import CourseList from "./components/course-list/CourseList";
import About from "./components/about-view/About";

const Routes = (props) => (
    <Router {...props}>
        <Route path="/" component={App}>
            <IndexRoute component={Login} />
            <Route path="/login" component={LoginView} />
            <Route path="/signup" component={SignupView} />
            <Route path="/courses" component={CourseList} />
            <Route path="/about" component={About}/>
            <Route path="/*" component={CourseList} />
        </Route>
    </Router>
);

export default Routes
