$( document ).ready(function() {
   	$(".after_word_is_added").css("display","none");
   	$(".after_word_is_removed").css("display","none");
   	 $(".after_word_is_exception").css("display","none");
});

function remove(obj)
{
	id = obj.getAttribute("data");
	$("#"+id).fadeOut(100);
}

function display_none(obj)
{
	alert(document.getElementById(obj.getAttribute('data')).style.display);
	$("#"+obj.getAttribute('data')).css("display","none");
}

function display_block(obj)
{
	$("#"+obj.getAttribute('data')).css("display","inherit");

}

function undo_button_clicked(obj)
{
	//alert("undo_button_clicked");
	//display_block(obj);
	$("#"+obj.getAttribute('data')).show();
	var tick_buttons = document.getElementsByClassName("after_word_is_removed");
	//$(".after_word_is_added").css("visibility","visible");

	var i;
	for(i=0;i<tick_buttons.length;i++)
	{
		//tick_buttons[i].css("visibility","visible");
		//alert(tick_buttons[i].getAttribute('data')+" #### "+obj.getAttribute('data'));
		if(tick_buttons[i].getAttribute('data')==obj.getAttribute('data'))
		{
			tick_buttons[i].style.display = 'none';
			//alert("hello");
			//alert(tick_buttons[i].innerHTML);
			break;
		}
	}
}

function remove_button_clicked(obj)
{
	//display_none(obj);
	$("#"+obj.getAttribute('data')).hide();
	var tick_buttons = document.getElementsByClassName("after_word_is_removed");
	//$(".after_word_is_added").css("visibility","visible");

	var i;
	for(i=0;i<tick_buttons.length;i++)
	{
		//tick_buttons[i].css("visibility","visible");
		//alert(tick_buttons[i].getAttribute('data')+" #### "+obj.getAttribute('data'));
		if(tick_buttons[i].getAttribute('data')==obj.getAttribute('data'))
		{
			tick_buttons[i].style.display = 'block';
			//alert("hello");
			//alert(tick_buttons[i].innerHTML);
			break;
		}
	}
}

function add_button_clicked(obj)
{
	//gets table
	//alert("add_button");
	var oTable = document.getElementById(obj.getAttribute('data'));
	//alert(document.getElementById(obj.getAttribute('data')).getAttribute('id'));
	//gets rows of table
	var rowLength = oTable.rows.length;
	var values=[];
	var names=[];

	//loops through rows    
	for (i = 0; i < rowLength-1; i++)
	{

	   //gets cells of current row
	   var oCells = oTable.rows.item(i).cells;

	   //gets amount of cells of current row
	   var cellLength = oCells.length;

	   //loops through each cell in current row
	   for(var j = 0; j < cellLength; j++)
	   {
	      /* get your cell info here */
	       var cellVal = oCells.item(j).children;
	       //alert(cellVal[0].getAttribute('name'));
	       names.push(cellVal[0].getAttribute('name'));
	       cellVal = cellVal[0].value;

	       values.push(cellVal);
	       //alert(cellVal);
	   }
	}

	//alert(values[0]);

	//alert("getting in django");
	//alert(values);

	var csrftoken = obj.getAttribute('token');
	var word_id;
	//alert(csrftoken);
	var temp_url = location.protocol + '//' + location.host  + obj.getAttribute('url');
	$.ajax({
        url: temp_url,
        //method: 'POST', // or another (GET), whatever you need
        //type: "POST",
        method:'POST',
          data: {
          	'values[]':values,
          	'names[]':names,
          	csrfmiddlewaretoken : csrftoken
         },
        success: function (data) {   
	        word_id = JSON.parse(data).word_id;     
	       //alert(JSON.parse(data).word_id+" is id of saved word");
	       	remove(obj);
			var tick_buttons = document.getElementsByClassName("after_word_is_added");
			//$(".after_word_is_added").css("visibility","visible");

			var i;
			for(i=0;i<tick_buttons.length;i++)
			{
				//tick_buttons[i].css("visibility","visible");
				//alert(tick_buttons[i].getAttribute('data')+" #### "+obj.getAttribute('data'));
				if(tick_buttons[i].getAttribute('data')==obj.getAttribute('data'))
				{
					tick_buttons[i].style.display = 'block';
					a_tag = tick_buttons[i].children[1];
					tick_buttons[i].children[0].innerHTML= values[0];
					a_tag.setAttribute("href",location.protocol + '//' + location.host+"/update-word-page/"+word_id);
					tick_buttons[i].setAttribute("word_id",word_id);
					//alert("hello");
					//alert(tick_buttons[i].innerHTML);
					break;
				}
			}
    	}
    });

}

function edit_button_clicked(obj)
{
	var tick_buttons_div = document.getElementsByClassName("after_word_is_added");
	//$(".after_word_is_added").css("visibility","visible");

	var temp_url = location.protocol + '//' + location.host  + obj.getAttribute('url');

	var i;
	for(i=0;i<tick_buttons_div.length;i++)
	{
		//tick_buttons[i].css("visibility","visible");
		//alert(tick_buttons[i].getAttribute('data')+" #### "+obj.getAttribute('data'));
		if(tick_buttons_div[i].getAttribute('data')==obj.getAttribute('data'))
		{
			
			// get url from the button
			var url = obj.getAttribute('url');

			// get id of word from tick_buttons_div
			var word_id = tick_buttons_div[i].getAttribute('word_id');
			break;
		}
	}
}

function exception_button_clicked(obj)
{
	$("#"+obj.getAttribute('data')).hide();
	var tick_buttons = document.getElementsByClassName("after_word_is_exception");
	var words = document.getElementsByName("word");
	//$(".after_word_is_added").css("visibility","visible");

	var i;
	var word;
	for(i=0;i<tick_buttons.length;i++)
	{
		//tick_buttons[i].css("visibility","visible");
		//alert(tick_buttons[i].getAttribute('data')+" #### "+obj.getAttribute('data'));
		if(tick_buttons[i].getAttribute('data')==obj.getAttribute('data'))
		{
			tick_buttons[i].style.display = 'block';
			tick_buttons[i].children[0].innerHTML= words[i].value;
			word = words[i].value;
			//alert("hello");
			//alert(tick_buttons[i].innerHTML);
			break;
		}
	}
	var csrftoken = obj.getAttribute('token');
	var temp_url = location.protocol + '//' + location.host  + obj.getAttribute('url');
	$.ajax({
        url: temp_url,
        //method: 'POST', // or another (GET), whatever you need
        //type: "POST",
        method:'POST',
          data: {
          	word:word,
          	csrfmiddlewaretoken : csrftoken
         },
        success: function (data) {        
          // alert(data);
        }
    });
}

function test(obj)
{
	//alert("csrf token is "+obj.getAttribute('token'));
	//var csrftoken = getCookie('csrftoken');
	var csrftoken = obj.getAttribute('token');
	var temp_url = location.protocol + '//' + location.host  + obj.getAttribute('url');
	$.ajax({
        url: temp_url,
        //method: 'POST', // or another (GET), whatever you need
        //type: "POST",
        method:'POST',
          data: {
          	name:'amit',
          	csrfmiddlewaretoken : csrftoken
         },
        success: function (data) {        
           alert(JSON.parse(data)[0].foo);
        }
    });
}

function myFunc(id)
{
	event.preventDefault();
	$(id).toggle(500);
}

function cross_button_clicked(obj)
{
	$("#red_cross_button").css("visibility","hidden");
	$("#new_passage_word_div").css("visibility","hidden");
	$("#new_passage_word_bottom").css("z-index","1");
}