import React from "react";

export const Button = ({type, text, styles, action}) => {
    return (
        <button type={type} className={["btn", styles].join(' ')} onClick={action}>
            {text}
        </button>
    );
};