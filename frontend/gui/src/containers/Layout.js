import React from 'react';

const CustomLayout = (props) => {
    return (
        <div>
            <h1>Sadar</h1>
            <div>
                {props.children}
            </div>
        </div>
    )
}

export default CustomLayout;
