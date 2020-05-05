import React from 'react';
import './App.css';
import CourseList from "./components/course-list/CourseList";
import {
    BrowserRouter as Router,
    Switch,
    Route,
    Link
} from "react-router-dom";
import About from "./components/About";
import Navbar from "react-bootstrap/Navbar";
import Nav from "react-bootstrap/Nav";
import 'bootstrap/dist/css/bootstrap.min.css';
import './index.css'
import Row from "react-bootstrap/Row";
import Container from "react-bootstrap/Container";
import Col from "react-bootstrap/Col";


function App() {
    return (
        <Router>
            <div>
                <Navbar bg="dark" variant="dark">
                    <Navbar.Brand href="/">Coursera</Navbar.Brand>
                    <Nav className="mr-auto">
                        <Nav.Link href="/">Courses</Nav.Link>
                        <Nav.Link href="/about">About</Nav.Link>
                    </Nav>
                </Navbar>

                <Container>
                    <Row>
                        <Col><Switch>
                            <Route path="/about">
                                <About />
                            </Route>
                            <Route path="/">
                                <CourseList />
                            </Route>
                        </Switch></Col>
                    </Row>
                </Container>

            </div>
        </Router>
    );
}

export default App;
