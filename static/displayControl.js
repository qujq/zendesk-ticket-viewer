function show_pervious_page(){
    page = page - 1
    requestBackend()
}

function show_next_page(){
    page = page + 1
    requestBackend()
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