import React from "react"

function Rudiobutton(props) {

    return (
            <div className="form-check">
                <input className="form-check-input" type="radio" name="flexRadioDefault" id="flexRadioDefault1"></input>
                <label className="form-check-label" >{props.value}</label>
            </div>
        )
    }

export default Rudiobutton;