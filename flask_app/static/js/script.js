

// FUNCTION FORM
function functForm() {
    var form = document.createElement('form');
    form.setAttribute('action', '/create/function');
    form.setAttribute('method', 'post');
    form.setAttribute('id', 'function-form')

    var formGroup1 = document.createElement('div')

    var labelName = document.createElement('label')
    labelName.setAttribute('for', 'name')
    labelName.innerText = 'Function Name:'

    var inputName = document.createElement('input')
    inputName.setAttribute('type', 'text')
    inputName.setAttribute('name', 'name')

    formGroup1.append(labelName, inputName)

    var formGroup2 = document.createElement('div')

    var labelLocation = document.createElement('label')
    labelLocation.setAttribute('for', 'location')
    labelLocation.innerText = 'Location:'

    var inputLocation = document.createElement('input')
    inputLocation.setAttribute('type', 'text')
    inputLocation.setAttribute('name', 'location')

    formGroup2.append(labelLocation, inputLocation)

    var formGroup3 = document.createElement('div')

    var labelDate = document.createElement('label')
    labelDate.setAttribute('for', 'date')
    labelDate.innerText = 'Date:'

    var inputDate = document.createElement('input')
    inputDate.setAttribute('type', 'date')
    inputDate.setAttribute('name', 'date')

    formGroup3.append(labelDate, inputDate)

    var formGroup4 = document.createElement('div')

    var labelAttire = document.createElement('label')
    labelAttire.setAttribute('for', 'attire')
    labelAttire.innerText = 'Attire:'

    var inputAttire = document.createElement('input')
    inputAttire.setAttribute('type', 'text')
    inputAttire.setAttribute('name', 'attire')

    formGroup4.append(labelAttire, inputAttire)

    var formGroup5 = document.createElement('div')

    var labelDescription = document.createElement('label')
    labelDescription.setAttribute('for', 'description')
    labelDescription.innerText = 'Description:'

    var inputDescription = document.createElement('textarea')
    inputDescription.setAttribute('name', 'description')
    inputDescription.setAttribute('col', '100')
    inputDescription.setAttribute('rows', '3')

    formGroup5.append(inputDescription)

    var sub = document.createElement('input')
    sub.setAttribute('type', 'submit')
    sub.setAttribute('class', 'btn btn-lg btn-dark btn-outline-info')

    form.append(formGroup1, formGroup2, formGroup3, formGroup4, labelDescription, formGroup5, sub)



    main = document.querySelector('.form-div');

    main.append(form);
    console.log(main)
    btn = document.querySelector('.funcBtn')
    btn.remove();

}


// CONVO FORM
function convoForm() {
    var form = document.createElement('form');
    form.setAttribute('action', '/create/convo');
    form.setAttribute('method', 'post');
    form.setAttribute('id', 'convo-form')

    var formGroup1 = document.createElement('div')

    var labelTopic = document.createElement('label')
    labelTopic.setAttribute('for', 'topic')
    labelTopic.innerText = 'Topic of Conversation:'

    var inputTopic = document.createElement('input')
    inputTopic.setAttribute('type', 'text')
    inputTopic.setAttribute('name', 'topic')

    formGroup1.append(labelTopic, inputTopic)

    var formGroup2 = document.createElement('div')

    var labelStarter = document.createElement('label')
    labelStarter.setAttribute('for', 'convo_starter')
    labelStarter.innerText = 'Conversation Starter:'

    var inputStarter = document.createElement('textarea')
    inputStarter.setAttribute('name', 'convo_starter')
    inputStarter.setAttribute('cols', '50')
    inputStarter.setAttribute('rows', '3')

    formGroup2.append(labelStarter)


    var sub = document.createElement('input')
    sub.setAttribute('type', 'submit')
    sub.setAttribute('class', 'btn btn-lg btn-dark btn-outline-info')

    form.append(formGroup1, formGroup2, inputStarter, sub)



    main = document.querySelector('.form-div-convo');

    main.append(form);
    console.log(main)
    btn = document.querySelector('.convoBtn')
    btn.remove();

}

// FUNCTIONS TABLE ROW POP-UP

function popUp(element) {
    element.setAttribute('id', 'rsvpBtn');

    var table = document.getElementById('functions-table');
    table.setAttribute('cls', 'black-out');


}

function popBack() {
    var btn = document.getElementById('rsvpBtn');
    btn.setAttribute('id', 'trow');
}


// COMMENTS

function getComments(convo_id) {
    data = { 'convo_id': convo_id }
    fetch(`http://localhost:5000/get_comments/${convo_id}`)
        .then(res => res.json())
        .then(data => {
            var container = document.getElementById('comment-feed')
            for (c = 0; c < data.length; c++) {
                var div = document.createElement('div')

                var commentHead = document.createElement('div')

                var comment = document.createElement('p')
                comment.innerText = c.comment

                div.append(comment)

                container.append(div)

            }
        })
}


function showComments(e) {
    // let response = await fetch(`http://localhost:5000/get_comments/${id}`);
    // let coderData = await response.json();
    // console.log(coderData)
    // console.log(typeof(coderData))
    // console.log("hello",convo_id)

    var form = document.getElementById('comment-form')


    var text = document.createElement('textarea')
    text.setAttribute('name', 'comment')
    text.setAttribute('placeholder', 'Leave a Comment...')
    text.setAttribute('rows', '4')
    // var input = document.getElementById('commentInput')
    //     input.setAttribute('type','text')

    var sub = document.createElement('input')
    sub.setAttribute('type', 'submit')
    sub.setAttribute('value', 'Comment')
    sub.setAttribute('class', 'btn btn-lg btn-light btn-outline-info')
    sub.setAttribute('form', 'comment-form')
    sub.setAttribute('id', 'commentSub')
    // sub.setAttribute('onclick','loadComments()')

    form.append(text, sub)

    e.replaceWith(form)

}

function displayComments(e) {
    var comments = document.getElementById('main-comment-div');
    comments.setAttribute('class', 'comment-section')

    e.remove();

}

// var commentForm = document.getElementById('comment-form');
// commentForm.onsubmit = function (e) {

//     e.preventDefault();

//     var form = new FormData(commentForm);

//     fetch("http://localhost:5000/create/comment", { method: 'POST', body: form })
//         .then(response => response.json())
//         .then(data => {
//             console.log(data)
//             var comments = document.getElementById('main-comment-div');

            // comments.;

            // var newProf = document.createElement('h3');
            //     newProf.innerHTML = data
            //     newProf.setAttribute('id','prof') 
            //     newProf.setAttribute('onclick','changeProfession(this)');
            //     newProf.setAttribute('class','btn btn-lg btn-dark btn-outline-info');
            // var sub = document.getElementById('sub')
            //     sub.setAttribute('type','hidden')

            // prof.replaceWith(newProf);
//         })

// }




// PROFILE

// ADD PROFESSION

function addProfession(e) {
    // var profession = document.getElementById('profession');

    var input = document.createElement('input')
    input.setAttribute('type', 'text')
    input.setAttribute('name', 'profession')
    input.setAttribute('id', 'prof')
    input.setAttribute('class', 'cursor-text')
    // input.setAttribute('form','form-profession')


    e.replaceWith(input)

    var sub = document.getElementById('sub')
    sub.setAttribute('type', 'submit')
    // sub.setAttribute('form','form-profession')
}
function changeProfession(e) {
    // var profession = document.getElementById('prof');

    var input = document.createElement('input')
    input.setAttribute('type', 'text')
    input.setAttribute('name', 'profession')
    input.setAttribute('id', 'prof')
    input.setAttribute('class', 'cursor-text')
    // input.setAttribute('form','form-profession')

    e.replaceWith(input)

    var sub = document.getElementById('sub')
    sub.setAttribute('type', 'submit')
    // sub.setAttribute('form','form-profession')
}

var formProfession = document.getElementById('add-profession');
formProfession.onsubmit = function (e) {

    e.preventDefault();

    var form = new FormData(formProfession);

    fetch("http://localhost:5000/update/profession", { method: 'POST', body: form })
        .then(response => response.json())
        .then(data => {
            console.log(data)
            var prof = document.getElementById('prof');

            var newProf = document.createElement('h3');
            newProf.innerHTML = data
            newProf.setAttribute('id', 'prof')
            newProf.setAttribute('onclick', 'changeProfession(this)');
            newProf.setAttribute('class', 'btn btn-lg btn-dark btn-outline-info');
            var sub = document.getElementById('sub')
            sub.setAttribute('type', 'hidden')

            prof.replaceWith(newProf);
        })

}


// CHANGE PROFILE PICTURE

function changePic() {
    var pic = document.getElementById('user-pic');
    pic.setAttribute('type', 'file');

    var sub = document.getElementById('submit');
    sub.setAttribute('type', 'submit')
    // upload = document.createElement('input')
}

// var formPic = document.getElementById('pic-form');
// formPic.onsubmit = function(e){

//     e.preventDefault();

//     var form = new FormData(formPic);

//     fetch("http://localhost:5000/picture", { method :'POST', body : form})
//         .then( response => response.json() )
//         .then( data => {
//             console.log(data) 
//             FileUpload1 = data
//             Fileuplaod1.saveAs(Server.Mappath("MyDash/flask_app/static/img") + FileUplaod1.FileName)
//         })

// }

// ADD NETWORK LINK

function addNetwork(e) {
    // var profession = document.getElementById('profession');
    var btn = e;

    var form = document.createElement('form')
    form.setAttribute('id', 'network-form')
    form.setAttribute('method', 'post')
    form.setAttribute('action', '/add/network')

    var formGroup1 = document.createElement('div')

    var labelNetwork = document.createElement('label')
    labelNetwork.setAttribute('for', 'network')


    var inputNetwork = document.createElement('input')
    inputNetwork.setAttribute('type', 'text')
    inputNetwork.setAttribute('name', 'network')
    inputNetwork.setAttribute('placeholder', 'Instagram, Linkedin, GitHub, etc...')
    inputNetwork.setAttribute('class', 'cursor-text')

    formGroup1.append(labelNetwork, inputNetwork)

    var formGroup2 = document.createElement('div')

    var labelUrl = document.createElement('label')
    labelUrl.setAttribute('for', 'url')

    var inputUrl = document.createElement('input')
    inputUrl.setAttribute('type', 'text')
    inputUrl.setAttribute('name', 'url')
    inputUrl.setAttribute('placeholder', '@JohnSmith')
    inputUrl.setAttribute('class', 'cursor-text')

    formGroup2.append(labelUrl, inputUrl)

    var sub = document.createElement('input')
    sub.setAttribute('type', 'submit')
    sub.setAttribute('class', 'btn btn-sm btn-dark btn-outline-info')
    sub.setAttribute('form', 'network-form')

    form.append(formGroup1, formGroup2, sub)

    e.replaceWith(form)
}


// ADD SKILL

function addSkill(e) {
    // var profession = document.getElementById('profession');
    var btn = e;

    var form = document.createElement('form')
    form.setAttribute('id', 'skill-form')
    form.setAttribute('method', 'post')
    form.setAttribute('action', '/add/skill')


    var input = document.createElement('input')
    input.setAttribute('type', 'text')
    input.setAttribute('name', 'skill')
    input.setAttribute('id', 'one_skill')
    input.setAttribute('class', 'cursor-text')



    var sub = document.createElement('input')
    sub.setAttribute('type', 'submit')
    sub.setAttribute('class', 'btn btn-sm btn-dark btn-outline-info')

    form.append(input, sub)
    e.replaceWith(form)
}

// var formSkill = document.getElementById('skill-form');
//     formSkill.onsubmit = function(e){

//     e.preventDefault();

//     var form = new FormData(formSkill);

//     fetch("http://localhost:5000/add/skill", { method :'POST', body : form})
//         .then( response => response.json() )
//         .then( data => {
//             console.log(data) 
//         })

// }






// PROJECT FORM

function addProject() {
    var form = document.createElement('form');
    form.setAttribute('action', '/create/project');
    form.setAttribute('method', 'post');
    form.setAttribute('id', 'project-form')

    var formGroup1 = document.createElement('div')
    formGroup1.setAttribute('class', 'form-details')

    var labelName = document.createElement('label')
    labelName.setAttribute('for', 'name')
    labelName.innerText = 'Project Name:'

    var inputName = document.createElement('input')
    inputName.setAttribute('type', 'text')
    inputName.setAttribute('name', 'name')

    formGroup1.append(labelName, inputName)


    var formGroup2 = document.createElement('div')

    var labelType = document.createElement('label')
    labelType.setAttribute('for', 'type')
    labelType.innerText = 'Type of Project:'

    var inputType = document.createElement('select')
    inputType.setAttribute('name', 'type')

    var optionType1 = document.createElement('option')
    optionType1.setAttribute('value', 'Solo')
    optionType1.innerHTML = 'Solo Project'

    var optionType2 = document.createElement('option')
    optionType2.setAttribute('value', 'Group')
    optionType2.innerHTML = 'Group Project'

    inputType.append(optionType1, optionType2)


    formGroup2.append(labelType, inputType)

    var formGroup3 = document.createElement('div')

    var labelSkills = document.createElement('label')
    labelSkills.setAttribute('for', 'skills')
    labelSkills.innerText = 'Skills Being Used:'

    var inputSkills = document.createElement('textarea')
    inputSkills.setAttribute('name', 'skills')
    inputSkills.setAttribute('cols', '50')
    inputSkills.setAttribute('rows', '3')

    formGroup3.append(labelSkills)

    var formGroup4 = document.createElement('div')

    var labelDescription = document.createElement('label')
    labelDescription.setAttribute('for', 'description')
    labelDescription.innerText = 'Describe Your Project:'

    var inputDescription = document.createElement('textarea')
    inputDescription.setAttribute('name', 'description')
    inputDescription.setAttribute('cols', '50')
    inputDescription.setAttribute('rows', '3')

    formGroup4.append(labelDescription)


    var sub = document.createElement('input')
    sub.setAttribute('type', 'submit')
    sub.setAttribute('class', 'btn btn-lg btn-dark btn-outline-info')

    form.append(formGroup1, formGroup2, formGroup3, inputSkills, formGroup4, inputDescription, sub)



    main = document.getElementById('project-form-div');

    main.append(form);
    console.log(main)
    btn = document.querySelector('.projectBtn')
    btn.remove();

}

