routerApp.controller('vnfimageController',['$scope','$location','$http',function(scope,loc,http){

	 scope.ipath ='upload.html'; 
	 scope.showtable=false;
	
	scope.imagename='';
	scope.filename=''; 
	scope.vnftype='';
	scope.vnftypeid='';
	
scope.onvimgtypeChange=function(vnftype){
	
	scope.vnftype=vnftype;
}
 scope.uploadImage = function(){ 

scope.imagename = event.target.files[0].name;
		
}
scope.uploadfile=function(){
	
	
	scope.filename = event.target.files[0].name;
}
scope.finalsubmit=function(rlsnms){
	var imgnm=scope.imagename;
	var filename=scope.filename;
	var vntp=scope.vnftype;
	var rlsname=rlsnms;
	scope.searchButtonText ='Searching';
	http({
            method: 'POST',
            url: 'http://localhost:8080/vnfUploadAll',
            headers: {
               'Content-Type': undefined
            },
            params: {
               
                imageName:  imgnm,
				flavfilename:filename,
				vnftypename:vntp,
				rlsname:rlsname
            }
        })
        .then(function (data) {
		
			var edata=JSON.stringify(data.data);
			if(edata.indexOf('Failed')>=0){
				
				scope.uploadedFilefailure = true;
				
			}
			else{ 
				scope.uploadedFileSuccess = true;
			}
			scope.searchButtonText ='stop';			
			scope.successmessage=data.data;
		
			
			
		
		});
	
}
scope.gotoimg1=function(valh){
	
	scope.ipath=valh;
	scope.showtable=false;
}
scope.onvvnftypeChange=function(vvnftype){
	scope.vnftypeid=vvnftype;
	http({
			url: "http://localhost:8080/vnfgetuploadimage",
			params: {vnfid: vvnftype}
			
			}).then(function (response) {
			var sdata=JSON.stringify(response.data);
			var cdata=JSON.parse(sdata);
			scope.vimfnames = cdata;
			
	}); 
	
}
scope.onvvimgChange=function(vimgnm){
	
	http({
			url: "http://localhost:8080/vnfUploadView",
			params: {ImageId: vimgnm,
					 vnftypeid:scope.vnftypeid}
			
			}).then(function (response) {
			var sdata=JSON.stringify(response.data);
			var cdata=JSON.parse(sdata);
			scope.vfnames = cdata;
			scope.showtable=true;
			
	}); 
}
scope.onvfavChange=function(flv){
	
}
}]);
