import React from "react";


export const RowTwoValues = ({ values }) => {
    
    return (
        <>
            <div className="row justify-content-center align-items-center g-2">
                {values.map((value, index) =>
                    <div className="col" key={index}>
                        <label className="form-label">{value.title}</label>
                        <p className="lead">{value.data}</p>
                    </div>
                )
                }
            </div>
            <hr />
        </>
    )
};

