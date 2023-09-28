



var table = $('#met_table').DataTable({
      fixedColumns: {
        left: 2
    },
    pageLength : 7,
    lengthMenu: [[7, 10, 20, 50], [7, 10, 20, 50]],
    "bPaginate": true,
    //"searching": false,
    "info":	true,
     "fixedHeader": true,
     "bFilter": true,
     "order": [[3, "desc"]],//default sorting

     "columnDefs": [
                  {"className": "dt-center", "targets": "_all"},
                  //stupid shit

                  {
                  "data": 8,
                 "targets": 8,
                 "render": function(data,type,full) {
                            return ('<a target="_blank" target="_blank" href="' + "/browse_metabolites/_" + full[0] + full[3].toString() + full[4] + '">' + data +"</a>").replace(',', '.'); // hmdb + pubmed + raw-p-val
                 },
               },
                 {


                     // The `data` parameter refers to the data for the cell (defined by the
                     // `data` option, which defaults to the column being worked with, in
                     // this case `data: 0`.


                     //ref to hmdb
                     "render": function ( data, type, row ) {
                       if (data != "–"){

                         return '<a class="btn btn-outline-primary" target="_blank" href="' + "http://www.hmdb.ca/metabolites/" + data+'">' + data +"</a>";
                       }
                       else if (data == "–"){

                         return '<div class="btn btn-primary" >' + data + "</div>";
                       }
                     },
                     "targets": 0
                 },
                 {
  								"targets": 1,
                  "data": 0,
  								"render": function(data,type,full) {
  									         return '<a target="_blank" target="_blank" href="' + "/browse_metabolites/" + data+'">' + full[1] +"</a>";
  								}
  							},

                ///arrows
                {
                 "targets": 2,
                 "data": 2,
                 "render": function(data,type,full) {
                            if (data == "up") return "↑";
                            else if (data == "down") return "↓";
                            else return data;
                 }
               },
               //pubmed
               {
                "targets": 3,
                "data": 3,
                "render": function(data,type,full) {
                           return '<a target="_blank" target="_blank" href="' + "/browse_studies/PUBMED" + data+'">' + data +"</a>";
                }
              },
                //p-val
                {
                "targets": 10,
                 "data": 10,
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
              //fdr
              {
              "targets": 11,
               "data": 11,
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
            //vip
            {
            "targets": 12,
             "data": 12,
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
           "targets": 13,
           "data": 3,
           "render": function(data,type,full) {
                      return '<a target="_blank" target="_blank" href="' + "/browse_metabolites/PUBMED" + data + "_mets" + '">' + full[13] +"</a>";
           },
         },
              ],
          "scrollY": true,




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
