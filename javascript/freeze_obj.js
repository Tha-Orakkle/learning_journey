function freezeObj() {
    "use strict";
    const MATH_CONST = {
        PI: 3.14
    };

    Object.freeze(MATH_CONST);

    try {
        MATH_CONST.PI = 99;
    } catch( ex ) {
        console.log("ex");
    }
    return MATH_CONST.PI;
}

console.log(freezeObj());