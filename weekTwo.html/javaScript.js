function login()
{
    document.querySelector("#loginButton").text = "Signout";
};

function likesOne()
{
    alert("Ninja was liked");
};

function removeButton() {
    try {
        document.querySelector(".addDef").remove();
    } catch (error) { }
};
