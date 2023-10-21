const errorMsg = (element, msg) => {
    element.style = "border: 4px solid red;";
    element.setCustomValidity(msg);
    element.reportValidity();
    return false;
};

const cleanError = (element) => {
    element.setCustomValidity("");
    element.style = "";
    return true;
};

const validateEmail = (email) => {
    let re = /^(?:(?!.*?[.]{2})[a-zA-Z0-9](?:[a-zA-Z0-9.+!%-]{1,64}|)|\"[a-zA-Z0-9.+!% -]{1,64}\")@[a-zA-Z0-9][a-zA-Z0-9.-]+(.[a-z]{2,}|.[0-9]{1,})$/;
    if(email.value.length == 0)
        return errorMsg(email,"Dato obligatorio.");
    if(email.value.length > 30)
        return errorMsg(email,"Excede largo maximo.");
    if(!re.test(email.value))
        return errorMsg(email,"Debe cumplir formato de dirección de correo electrónico. ej: 'usuario@correo.com' ");
    return cleanError(email);
};

const validateSports = (sports) => {
    const selectedOptions = Array.from(sports.selectedOptions).map(option => option.value);
    if(selectedOptions.length < 1 || 3 < selectedOptions.length )
        return errorMsg(sports, "Dato obligatorio. Al menos 1 y máximo 3.");
    for( let sport of selectedOptions){
        if(!Sports.includes(sport))
            return errorMsg(sports, "Dato obligatorio. Al menos 1 y máximo 3.");
    }
    return cleanError(sports);
};

const validateRegion = (region) => {
    if( 0 < region.value.length)
        return cleanError(region);
    return errorMsg(region, "Dato obligatorio.");
};

const validateComuna = (comuna) => {
    if (0 < comuna.value.length)
        return cleanError(comuna);
    return errorMsg(comuna,"Dato obligatorio.");
};

const validateTransport = (transport) => {
    if (0 < transport.value.length)
        return cleanError(transport);
    return errorMsg(transport, "Dato obligatorio.");
};

const validateName = (name) => {

    let re = /^[\wñáéíóúÁÉÍÓÚ]+([ ]{0,1}[\wñáéíóúÁÉÍÓÚ]+)*$/;
    if (!(3 <= name.value.length && name.value.length <= 80))
        return errorMsg(name, "Dato Obligatorio. Largo mínimo 3, máximo 80.");
    if(!re.test(name.value))
        return errorMsg(name,"Formato incorrecto")
    return cleanError(name);
};

const validatePhoneNumber = (phone) => {
let re = /^(([+]{0,1}5{1}6{1}[ ]{0,1}9{1}[ ]{0,1})|(9{1}[ ]{0,1})|())[1234567890]{4}[-]{0,1}[1234567890]{4}$|^$/;
    if(phone.value.length == 0 || (phone.value.length < 16 && re.test(phone.value)))
        return cleanError(phone);
    return errorMsg(phone, "Debe cumplir con formato de número de teléfono móvil.");
};

const validateCraft = (crafts) => {
    const selectedOptions = Array.from(crafts.selectedOptions).map(option => option.value);

    if(selectedOptions.length < 1 || 3 < selectedOptions.length )
        return errorMsg(crafts, "Dato obligatorio. Al menos 1 y máximo 3.");
    for( let craft of selectedOptions){
        if(!Artesanias.includes(craft))
            return errorMsg(crafts, "Dato obligatorio. Al menos 1 y máximo 3.");
    }
    return cleanError(crafts);
};

const validateDescription = (desc) =>{
    if (desc.value.length < (4*50+1))
        return cleanError(desc);
    return errorMsg(desc, "Excede largo.");
};

const validateComment = (comment) => {
    if (comment.value.length < 81)
        return cleanError(comment);
    return errorMsg(comment, "Excede largo.")
};

const validateFiles = (files) => {
    if (!files.files) return false;

    let validLength = (0 < files.files.length) && (files.files.length < 4);
    let validType = true;
    for(const file of files.files){
        let fileFamily = file.type.split("/")[0];
        validType &&= fileFamily == "image" || file.type == "application/pdf";
    };
    if (validLength && validType)
        return cleanError(files);
    return errorMsg(files,"Obligatorio. Mínimo 1, máximo 3.");
};