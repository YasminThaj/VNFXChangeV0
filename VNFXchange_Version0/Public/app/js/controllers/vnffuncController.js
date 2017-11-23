routerApp.controller('vnffuncController',['$scope','$location','$http',function(scope,loc,http){
	
	scope.fpath ='testcases.html';
	scope.nval=true;	
	scope.selectedvnfname='';
	scope.gotofun1=function(fpath){
	scope.nval=true;
	scope.isDisabled = false;
		scope.fpath=fpath;

		
	}
	scope.isDisabled = false;
	scope.gotoexecute =function()
	{   
	    console.log("gotoexecute");
		scope.isDisabled = true;
		scope.searchButtonText="Searching";
		document.getElementById('tstbutn').value="Executing ...";
		document.getElementById('tstbutn').style.margin="-7px 0 0 0";
		
		http.get("http://localhost:8080/vnfexecute")
		.then(function (response) {
		console.log("executedata"+response.data);
		scope.nval=false;
	//			http.get("http://localhost:8080/vnfreport")
	//			.then(function (response) {
	//			console.log("reportdata"+response.data);	
			
				setTimeout(function () {
		  scope.$apply(function(){
			  scope.searchButtonText="false";
			scope.names = response.data;
			scope.report = response.report;
			
		document.getElementById('rep').className='active';
		document.getElementById('test').className='';
		scope.fpath='reports.html';
		  });
		}, 2000);
		
				
		
  //  });
					

			
		});
		
		
		
    }
	scope.ontypeChange =function(sname){

	
		scope.showdrdwn=true;
		
		
	
	


	
}
	scope.onnameChange=function(vname){
	
	scope.ontestChange = function(selectedtestName) {
    console.log(selectedtestName);
	scope.selectedvnfname=selectedtestName;
	if (selectedtestName=="demo1")
	{

	scope.showcheckbox=true;
	scope.showbtn=true;
	}
}
	
		scope.showsanrdwn=true;
		
	
		
/* <!-- scope.showbtn=true; --> */

}

scope.ontestChange=function(tname){
/* <!-- scope.showbtn=true; --> */
}
	
	}]);
	