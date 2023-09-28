




$(document).ready( function () {
///////////////////////////////
var table = $('#met_table').DataTable({

      fixedColumns: {
        left: 2
    },
    pageLength : 5,
    lengthMenu: [[5, 10, 20, 50], [5, 10, 20, 50]],
    "bPaginate": true,
    //"searching": false,
    "info":	true,
     "fixedHeader": true,
     "bFilter": true,
     "order": [[0, "desc"]],//default sorting
     "scrollX": true,
     "scrollY": true,


     "columnDefs": [
                  {"className": "dt-center", "targets": "_all"},



                ///arrows
                {
                 "targets": 2,
                 "data": 2,
                 "render": function(data,type,full) {
                            if (data.includes("up") || data.includes("↑")) {return "↑"}
                            else if (data.includes("down") || data.includes("↓")) {return "↓"}
                            else {return data;}
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
              //stupid shit

              {
              "data": 5,
             "targets": 5,
             "render": function(data,type,full) {
                        return ('<a target="_blank" target="_blank" href="' + "/browse_metabolites/_" + full[0] + full[2].toString() + full[3] + '">' + data +"</a>").replace(',', '.'); // hmdb + pubmed + raw-p-val
             },
           },
                //p-val
                {
                "targets": 5,
                 "data": 5,
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
              "targets": 6,
               "data": 6,
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
            "targets": 7,
             "data": 7,
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
           "targets": 9,
           "data": 3,
           "render": function(data,type,full) {
                      return '<a target="_blank" target="_blank" href="' + "/browse_metabolites/PUBMED" + data + "_mets" + '">' + full[9] +"</a>";
           },
         },
          ],
          //"scrollY":   true,
    //"scrollX":        true,


          "buttons": [
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
      "select": true,

      "dom": 'Brtlip',
      "initComplete": function () {
                this.api()
                    .columns([1])
                    .every(function () {
                        var column = this;
                        var select = $('<select><option value=""></option></select>')
                            .appendTo("#super_class")
                            .on('change', function () {
                                var val = $.fn.dataTable.util.escapeRegex($(this).val());

                                column.search(val ? '^' + val + '$' : '', true, false).draw();
                            });

                        column
                            .data()
                            .unique()
                            .sort()
                            .each(function (d, j) {
                                select.append('<option value="' + d + '">' + d + '</option>');
                            });

                    });
            },

});

table.columns( [1] ).visible( false );
} );
