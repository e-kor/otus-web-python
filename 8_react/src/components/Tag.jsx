import React from 'react';

const Tag = props => {
    const {name} = props;

    return (
        <small className="tag">#{name} </small>

    )
}

export default Tag;
