let user = {
    name: "Johnny",
    years: 9
};

let { name, years: age, isAdmin = false } = user;

alert(name); // Johnny
alert(age); // 9
alert(isAdmin); // false
