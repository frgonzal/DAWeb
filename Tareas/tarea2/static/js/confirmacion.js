const postForm = () => {
    if(validateForm()){
        document.getElementById("myForm").submit();
    }else{
        document.getElementById("containerRegreso").style.display = "none";
        document.getElementById("containerForm").style.display = "flex";
        document.getElementById("confirmacionSubmit").style.display = "none";
        document.getElementById("submitBtn").style.display = "flex";
    }
}

const validate = () => {
    if (validateForm()){
        document.getElementById("confirmacionSubmit").style.display = "flex";
        document.getElementById("containerForm").style.display = "none";
    }
};

const formConfirmar = () => {
    document.getElementById("containerRegreso").style.display = "flex";
    document.getElementById("confirmacionSubmit").style.display = "none";
    document.getElementById("containerForm").style.display = "none";
};

const formRechazar = () => {
    document.getElementById("containerForm").style.display = "flex";
    document.getElementById("confirmacionSubmit").style.display = "none";
    document.getElementById("submitBtn").style.display = "flex";
};