import React from 'react';
import './Tag.css'

const Tag = props => {
    const {name} = props;

    return (
        <small className="tag">#{name} </small>
    )
};

export default Tag;
