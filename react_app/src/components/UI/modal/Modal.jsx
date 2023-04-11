import React from "react";
import ReactDOM from 'react-dom';

const Modal = ({children, isVisable}) => {
    if (!isVisable) {
        return null;
    };

    return ReactDOM.createPortal(
        <div className="modal fade show" id="exampleModal" aria-labelledby="exampleModalLabel" aria-hidden="true" style={{display: "block"}}>
            {children}
        </div>
        , document.querySelector("#modal")
    )
};

export default Modal;
