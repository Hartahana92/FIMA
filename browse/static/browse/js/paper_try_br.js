var table = $('#table1').DataTable({
        fixedColumns: {
          left: 1
      },
      pageLength : 10,
      lengthMenu: [[10, 20, 50], [10, 20, 50]],
      "bPaginate": true, //
	  	//"searching": false, //
	  	"info":	true, //
	     "fixedHeader": true, //
       "bFilter": true,
       "bProcessing": true,
       "columnDefs": [
                  //p-val
                  {
                  "targets": 1,
                   "data": 1,
                  "render": function(data,type,full) {
                            var r = parseFloat(data.replace(',', '.'))
                            if (!isNaN(r)) {
                              if(r > 0.01) {
                                       return Number.parseFloat(r).toFixed(2);
                               }
                             else {
                                 if (r > 0.001){
                                     return "<0.01";
                                 }
                                 else {
                                     if (r > 0.0001) {
                                         return "<0.001";
                                     }
                                     else {
                                         return "<0.0001";
                                     }
                                 }
                             }
                           }
                           else {
                             return data;
                           }
                   }
                },
                {
                "targets": 2,
                 "data": 2,
                "render": function(data,type,full) {
                          var r = parseFloat(data.replace(',', '.'))
                          if (!isNaN(r)) {
                            if(r > 0.01) {
                                     return Number.parseFloat(r).toFixed(2);
                             }
                           else {
                               if (r > 0.001){
                                   return "<0.01";
                               }
                               else {
                                   if (r > 0.0001) {
                                       return "<0.001";
                                   }
                                   else {
                                       return "<0.0001";
                                   }
                               }
                           }
                         }
                         else {
                           return data;
                         }
                 }
              },
              {
              "targets": 3,
               "data": 3,
              "render": function(data,type,full) {
                        var r = parseFloat(data.replace(',', '.'))
                        if (!isNaN(r)) {
                          if(r > 0.01) {
                                   return Number.parseFloat(r).toFixed(2);
                           }
                         else {
                             if (r > 0.001){
                                 return "<0.01";
                             }
                             else {
                                 if (r > 0.0001) {
                                     return "<0.001";
                                 }
                                 else {
                                     return "<0.0001";
                                 }
                             }
                         }
                       }
                       else {
                         return data;
                       }
               }
            },
            {
            "targets": 4,
             "data": 4,
            "render": function(data,type,full) {
                      var r = parseFloat(data.replace(',', '.'))
                      if (!isNaN(r)) {
                        if(r > 0.01) {
                                 return Number.parseFloat(r).toFixed(2);
                         }
                       else {
                           if (r > 0.001){
                               return "<0.01";
                           }
                           else {
                               if (r > 0.0001) {
                                   return "<0.001";
                               }
                               else {
                                   return "<0.0001";
                               }
                           }
                       }
                     }
                     else {
                       return data;
                     }
             }
          },
      {
       "targets": 0,
       "data": 5,
       "render": function(data,type,full) {
                  return '<a target="_blank" target="_blank" href="' + "/browse_metabolites/" + data+'">' + full[0] +"</a>";
       },
     },
     {
                     "targets": [5],
                     "visible": false,

                 },],

       "dom": 'rtlip'
});




var table2 = $('#table2').DataTable({
        fixedColumns: {
          left: 1
      },
      pageLength : 10,
      lengthMenu: [[10, 20, 50], [10, 20, 50]],
      "bPaginate": true, //
      "bAutoWidth": false,

	  	//"searching": false, //
	  	"info":	true, //
	     "fixedHeader": true, //
       "bFilter": true,
       "bProcessing": true,
       "columnDefs": [
       {
        "targets": 0,
        "data": 6,
        "render": function(data,type,full) {
                   return '<a target="_blank" target="_blank" href="' + "/browse_metabolites/" + data+'">' + full[0] +"</a>";
        },

      },
      {
                 "targets": [6],
                 "visible": false,
             },],

             buttons: [
                   {
                           extend: 'print',
                           text: 'Print all',
                             exportOptions: {
                                 modifier: {
                                   selected: null
                             }
                         }
                     },
                 {
                     extend: 'print',
                     text: 'Print selected'
                 }
             ],
             select: true,

             "dom": 'Brtlip'
});
