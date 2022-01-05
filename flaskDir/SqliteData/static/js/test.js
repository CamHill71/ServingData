





(function(){
  "use strict"
  let url = "http://127.0.0.1:5000/api/cpu-load/1"; //"https://reqres.in/api/users"; //apps chart url
  let method = "GET";
  let typeOfResponse = "json";

  let xhr = new XMLHttpRequest();
  xhr.open(method,url,true);
  xhr.responseType = typeOfResponse;    
  xhr.send();
  
  xhr.onload = () => {      
      let responseObj =   xhr.response
      console.log(xhr.response)

      if (xhr.status != 200){
          alert(`Error ${xhr.status}: ${xhr.statusText}`);
      } else{
          alert(`Done, got ${xhr.response} bytes`);            
      }
     
      for(let responseNumber in responseObj){
          //alert("we have a responce")
          let response = responseObj[responseNumber]
          console.log(response.created_at)
          console.log(response.load )
      }
  }



}())




