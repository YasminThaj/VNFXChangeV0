routerApp.controller('onbordingcontroller',['$scope', '$sce','$http',function(scope,sce,http)
{
	/* $scope.url = $sce.trustAsResourceUrl('http://10.168.255.252:8080/VNF_AUTO_KVM/displayVm.action');
    $scope.changeIt = function () 
	{
        $scope.url = $sce.trustAsResourceUrl('https://www.google.co.in/');
	} */
	scope.imagename='';
	scope.flvname='';
	scope.vtype='';
	scope.offboardvtype='';
	scope.oppathname='VNF Onboard Upload';
	scope.onpath='vnfgonboard.html';
	scope.vnfNames='';
	scope.offboardMessage='';
	scope.gotoonbrd=function(valoh){
		scope.onpath=valoh;		
		if(valoh=='vnfgonboard.html'){scope.oppathname="VNF OnBoard"}else{scope.oppathname="VNF OffBoard"}
		
	}
	scope.onvnftypechange=function(vtype){

		console.log(vtype);
		scope.vtype=vtype;
		var cvtype=vtype.split(',');
	http({
			url: "http://localhost:8080/getOnboardImg",
			params:{vnftype:cvtype[0]}
			
			}).then(function (response) {
				
				console.log(JSON.stringify(response));
				var odata=JSON.stringify(response.data);
				var ojdata=JSON.parse(odata);
			scope.onimages = ojdata;
			
	}); 
	}
	scope.onimageChange=function(oflvid){
		console.log(oflvid);
		scope.imagename=oflvid;
		//var cimid=oflvid.split(',');
		http({
			url: "http://localhost:8080/getOnboardFlv",
			params:{ImageId:oflvid}
			
			}).then(function (response) {
				
				console.log(JSON.stringify(response));
				var odata=JSON.stringify(response.data);
				var ojdata=JSON.parse(odata);
			scope.onflvs = ojdata;
			
	}); 
	}
	scope.onbrdflvChange=function(flavour){
		
		scope.flvname=flavour;
	}
	
	
	scope.onboardfile=function(inname){
		
		var flvr=scope.flvname;		
		var imgn=scope.imagename;		
		var vnfname=inname;
		var vnftype=scope.vtype;
		var cdvnftype=vnftype.split(",");
		scope.searchButtonText ='seraching';
		
		http({
			url: "http://localhost:8080/vnfonboardimage",
			method:"POST",
			params:{onboard_image:imgn,onboard_flavour:flvr,onboard_vnfname:vnfname,vnftypename:cdvnftype[1],vnftypeid:cdvnftype[0]}
			
			}).then(function (response) {
			var odata=JSON.stringify(response.data);
			console.log("----------"+ response.data);
			if(odata.indexOf('Failed')>=0){
				
				scope.onboardFileFailure = true;
				
			}
			else{ 
				scope.onboardFileSuccess = true;
			} 
			scope.searchButtonText ='stop';
			scope.osuccessmessage=response.data;				
				//scope.onbrdimgdt = ojdata;
			
	}); 
	}
	
	scope.offboardVnftypeChange=function(selectedovnftype){		
		
		//var vnftype=scope.selectedovnftype;
		//var cdvnftype=vnftype.split(",");
		//console.log(flvr+imgn+cdvnftype[0]+cdvnftype[1]+inname);
		var VnfTypeId=1;
			scope.offboardvtype=selectedovnftype;
				
		http({
			url: "http://localhost:8080/vnfOffboardNames",
			method:"GET",		
			params:{VnfTypeId:VnfTypeId}
			
			}).then(function (response) {
				
				console.log(JSON.stringify(response.data));	
				var data=JSON.stringify(response.data);					
				var ojdata=JSON.parse(data);				
				scope.vnfNames = ojdata;
				
			
	}); 
	}
	
	scope.offboardfile=function(offboardvtype,selectedoVNFName){		
		var VnfName=selectedoVNFName;
		//console.log(JSON.stringify(VnfName));	
		 var vnftype=offboardvtype;
		var VnfTypeId=vnftype.split(",");
		console.log(VnfName+VnfTypeId[0]+VnfTypeId[1]);
		//var VnfTypeId=1;
		//var VnfName="Demo1";
		console.log("controller");
		
		http({
			url: "http://localhost:8080/vnfOffboardView",
			method:"GET",
			//params:{vnfname,vnftypename:cdvnftype[1],vnftypeid:cdvnftype[0]}
			params:{VnfName:VnfName,VnfTypeId:VnfTypeId[0]}
			
			}).then(function (response) {
				
				console.log(JSON.stringify(response.data));	
				var data=JSON.stringify(response.data);	
				var ojdata=JSON.parse(data);
				if(data.indexOf('Failed')>=0){
				
				scope.offboardFileFailure = true;
				
			}
			else{ 
				scope.offboardFileSuccess = true;
			} 				
				scope.offboardMessage = ojdata;
			
	}); 
	}
	
}]);