
        new Vue({
            el: "#app",
            data: {
                search: "",
                random_lists: [],
            },
            beforeMount() {
                this.getData();
            },
            methods: {
                getData() {
                    var self = this;
                    var url = "/dashboard/patients/api/patients/?";

                    if(self.search) {
                        url += "search=" + self.search;
                    }
                    $.get(url)
                        .done(function (response) {
                            self.random_lists = response;
                        })
                },

            },
            watch:{
                "search": function (){
                    this.getData();
                }
            }

        })




