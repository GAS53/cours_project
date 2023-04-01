import { useState } from "react";

const useModal = () => {
    const [isVisable, setIsVisable] = useState(false)

    const togleVisable = () => {
        setIsVisable(!isVisable)
    }
    return [isVisable, togleVisable]
};

export default useModal;