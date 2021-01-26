import React from 'react';
import { Menu, MenuItem } from '@material-ui/core';

const CustomLayout = (props) => {
    return (
        <div>
            <h1>Hello</h1>
            <div>
                {props.children}
            </div>
        </div>
    )
}

export default CustomLayout;
