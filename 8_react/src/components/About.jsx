import React from 'react';
import Form from "react-bootstrap/Form";
import Button from "react-bootstrap/Button";
import "./About.css"

const About = props => {
    return (
        <div>
            <h1>About</h1>
            <div className="about__aboutus"> Кто мы?
                Не знаем!
                Чего мы хотим?
                Всего!
                Когда мы хотим?
                Сейчас!
            </div>
            <Form className="contact-form">
                <h2>Contact us</h2>
                <Form.Group>
                    <Form.Label>your mail address</Form.Label>
                    <Form.Control type="email" placeholder="name@example.com"/>
                </Form.Group>
                <Form.Group>
                    <Form.Label>Message to us</Form.Label>
                    <Form.Control as="textarea" rows="3"/>
                </Form.Group>
                <Form.Group>
                    <Button variant="primary" size="lg">Отправить</Button>
                </Form.Group>
            </Form>
        </div>
    )
};

export default About;
