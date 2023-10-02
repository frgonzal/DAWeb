const formConfirmar = () => {
    document.getElementById("containerRegreso").style.display = "flex";
    document.getElementById("confirmacionSubmit").style.display = "none";
    document.getElementById("containerForm").style.display = "none";
};

const formRechazar = () => {
    document.getElementById("containerForm").style.display = "flex";
    document.getElementById("confirmacionSubmit").style.display = "none";
    document.getElementById("submit").style.display = "flex";
};