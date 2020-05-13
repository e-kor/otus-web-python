import React from 'react';
import Button from '@material-ui/core/Button';
import {TextValidator, ValidatorForm} from 'react-material-ui-form-validator';
import Grid from '@material-ui/core/Grid';
import Typography from '@material-ui/core/Typography';
import APIService from "../APIservice";

class ContactForm extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            email: "",
            body: ""
        };
        this.apiService = new APIService();
    }

    handleEmailChange = (event) => {
        // const email = event.target.value;
        // console.log(event.target);
        this.setState({email: event.target.value});
    }

    handleMessageChange = (event) => {
        // const email = event.target.value;
        // console.log(event.target);
        this.setState({body: event.target.value});
    }

    handleSubmit = () => {
        console.log(this.state)
        this.apiService.sendFeedback(this.state)
    }

    render() {
        const {email, body} = this.state;
        return (

            <ValidatorForm
                ref="form"
                onSubmit={this.handleSubmit}
                onError={errors => console.log(errors)}
            ><Typography component="h1" variant="h5">
                Свяжитесь с нами
            </Typography>
                <Grid container spacing={2}>
                    <Grid item xs={12}>
                        <TextValidator
                            label="Email"
                            onChange={this.handleEmailChange}
                            name="email"
                            value={email}
                            validators={['required', 'isEmail']}
                            errorMessages={['this field is required', 'email is not valid']}
                            variant="outlined"
                            required
                            fullWidth
                        />
                    </Grid>
                    <Grid item xs={12}>
                        <TextValidator
                            label="Your message"
                            onChange={this.handleMessageChange}
                            name="message"
                            value={body}
                            validators={['required']}
                            errorMessages={['this field is required']}
                            multiline={true}
                            rows={10}
                            variant="outlined"
                            required
                            fullWidth
                        />
                    </Grid>

                    <Button
                        type="submit"
                        fullWidth
                        variant="contained"
                        color="primary"
                    >
                        Отправить
                    </Button>

                </Grid>
            </ValidatorForm>
        );
    }
}

export default ContactForm;
