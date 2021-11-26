var page = 1
var per_page = 2
const BACKEND_BASE_URL = "http://localhost:8000"

window.onload = function () {
    backToList()
    var next_page_button = document.getElementById("next_page")
    var pervious_page_button = document.getElementById("pervious_page")
    next_page_button.style.display="none"
    pervious_page_button.style.display="none"
    requestBackend()    
}

function show_pervious_page(){
    page = page - 1
    requestBackend()
}

function show_next_page(){
    page = page + 1
    requestBackend()
}

function requestBackend(){
    var backend_url = BACKEND_BASE_URL + "/getTicket?"
    backend_url += "page=" + page + "&per_page=" + per_page
    var response = fetch(backend_url)
    response.then(res => res.json())
            .then(function(ticket_list){
                console.log(ticket_list)
                if(ticket_list.hasOwnProperty("error")){
                    var ticket_number = document.getElementById('ticket_number');
                    ticket_number.innerHTML = '<p style="color: red; font-size: 30px; font-family: "Times New Roman", Times, serif;">' + "Some errors occur: " + ticket_list.error + '</p>'
                }
                else if(ticket_list.hasOwnProperty("count")){
                    // display num of tickets
                    var ticket_number_block = document.getElementById('ticket_number');
                    var num_ticket = ticket_list.count
                    ticket_number_block.innerHTML = '<p style="font-size: 30px; font-family: "Times New Roman", Times, serif;">'
                            + num_ticket + ' total tickets, ' + ticket_list.tickets.length + ' on this page.' + '</p>'
                    
                    // pagination
                    pagination(num_ticket)                    

                    // display list of ticket subjects
                    if(ticket_list.hasOwnProperty("tickets")){
                        var ticket_list_block = document.getElementById('ticket_list');
                        var ticket_array = ticket_list.tickets
                        ticket_list_block.innerHTML = ''
                        for(var index = 0; index < ticket_array.length; ++index){
                            ticket_list_block.innerHTML += '<div style="margin-bottom: 1%; background-color: rgb(229, 231, 231); font-size: 25px; font-family: "Times New Roman", Times, serif;">'
                                + '<a onClick="displaySelectedTicket(' + ticket_array[index].id + ')">' 
                                + '[' + ticket_list.tickets[index].status + '] ' 
                                + ticket_list.tickets[index].subject + '</a>' + '</div>'
                        }
                    }
                    else{
                        alert("No tickets")
                    }                        
                }                    
                else{
                    var ticket_number = document.getElementById('ticket_number');
                    ticket_number.innerHTML = '<p style="color: red; font-size: 30px; font-family: "Times New Roman", Times, serif;">' + 'Some errors occur. We did not get number of tickets' + '</p>'
                }
                
            }
)}

function pagination(num_ticket){
    var next_page_button = document.getElementById("next_page")
    var pervious_page_button = document.getElementById("pervious_page")
    // Need page
    if(num_ticket > per_page){                            
        // hide all buttons
        next_page_button.style.display="none"
        pervious_page_button.style.display="none"
        // show next page            
        if(page * per_page < num_ticket){ 
            next_page_button.style.display="block"
            console.log("next")
        }
        // show previous page        
        if(page > 1){                                                        
            pervious_page_button.style.display="block"
            console.log("prev")
        }
    }
    // No need to page
    else{
        next_page_button.style.display="none"
        pervious_page_button.style.display="none"
    }
}

function requestUserName(user_id){
    var backend_url = BACKEND_BASE_URL + "/getUserName?"
    backend_url += "user_id=" + user_id
    var response = fetch(backend_url)
    response.then(res => res.json())
            .then(function(user_data){
                if(user_data["user"].hasOwnProperty("name")){
                    console.log(user_data["user"]["name"])
                    var ticket_requester_block = document.getElementById("ticket_requester")
                    ticket_requester_block.innerHTML = "<p> Requester: " + user_data["user"]["name"] + " </p>"
                }
                else{
                    var ticket_requester_block = document.getElementById("ticket_requester")
                    ticket_requester_block.innerHTML = "<p> Requester Not Found </p>"
                }  
                displayDetail()                
            })
}

function displaySelectedTicket(ticket_id){
    var backend_url = BACKEND_BASE_URL + "/getSelectedTicket?"
    backend_url += "ticket_id=" + ticket_id
    var response = fetch(backend_url)
    response.then(res => res.json())
            .then(function(ticket_content){
                console.log(ticket_content)
                if(ticket_content["ticket"].hasOwnProperty("requester_id")){
                    requestUserName(ticket_content["ticket"]["requester_id"])
                }
                else{
                    alert("No ticket id")
                }
                if(ticket_content["ticket"].hasOwnProperty("subject")){
                    var ticket_subject = ticket_content["ticket"]["subject"];
                    console.log("ticket_subject", ticket_subject);
                    var ticket_subject_block = document.getElementById("ticket_subject")
                    ticket_subject_block.innerHTML = "<p>" + ticket_subject + "</p>";
                }
                else{
                    alert("No ticket subject")
                }
                if(ticket_content["ticket"].hasOwnProperty("subject")){
                    var ticket_subject = ticket_content["ticket"]["subject"];
                    console.log("ticket_subject", ticket_subject);
                    var ticket_subject_block = document.getElementById("ticket_subject")
                    ticket_subject_block.innerHTML = "<p>" + ticket_subject + "</p>";
                }
                else{
                    alert("No ticket subject")
                }
                if(ticket_content["ticket"].hasOwnProperty("description")){
                    var ticket_description = ticket_content["ticket"]["description"];
                    console.log("ticket_description", ticket_description);
                    var ticket_description_block = document.getElementById("ticket_description")
                    ticket_description_block.innerHTML = "<p>" + ticket_description + "</p>";
                }
                else{
                    alert("No ticket subject")
                }
                var tickets_block = document.getElementById("tickets")
                tickets_block.style.display="none"
            })
}

function displayDetail(){
    var tickets_block = document.getElementById("tickets")
    tickets_block.style.display="none"
    var ticket_content_block = document.getElementById("ticket_content")
    ticket_content_block.style.display="block"
}

function backToList(){
    var tickets_block = document.getElementById("tickets")
    tickets_block.style.display="block"
    var ticket_content_block = document.getElementById("ticket_content")
    ticket_content_block.style.display="none"
}