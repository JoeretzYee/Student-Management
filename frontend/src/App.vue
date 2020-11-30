<template>
    <div id="app">
        <form @submit.prevent="submitForm">
            <div class="form-group row">
                <input
                    type="text"
                    placeholder="Name:"
                    class="form-control col-3 mx-2"
                    v-model="student.name"
                />
                <input
                    type="text"
                    placeholder="Course:"
                    class="form-control col-3 mx-2"
                    v-model="student.course"
                />
                <input
                    type="number"
                    placeholder="Rating:"
                    class="form-control col-3 mx-2"
                    v-model="student.rating"
                />

                <button type="submit" class="btn btn-success">Add</button>
            </div>
        </form>

        <table class="table table-dark text-center">
            <thead>
                <th>Name</th>
                <th>Course</th>
                <th>Rating</th>
            </thead>
            <tbody>
                <tr
                    v-for="student in students"
                    v-bind:key="student.id"
                    @dblclick="$data.student = student"
                >
                    <td>{{ student.name }}</td>
                    <td>{{ student.course }}</td>
                    <td>{{ student.rating }}</td>
                    <td>
                        <button
                            class="btn btn-danger btn-sm mx-1"
                            @click="deleteStudent(student)"
                        >
                            Delete
                        </button>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
export default {
    name: "App",
    data() {
        return {
            students: [],
            student: {},
        };
    },
    async created() {
        await this.getStudents();
    },
    methods: {
        submitForm() {
            if (this.student.id === undefined) {
                this.createStudent();
            } else {
                this.editStudent();
            }
        },
        async getStudents() {
            let response = await fetch("http://127.0.0.1:8000/api/students/");
            this.students = await response.json();
        },
        async createStudent() {
            await this.getStudents();

            let response = await fetch("http://127.0.0.1:8000/api/students/", {
                method: "post",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(this.student),
            });
            await this.getStudents();
            this.student.name = "";
            this.student.course = "";
            this.student.rating = "";
        },
        async editStudent() {
            await this.getStudents();

            let response = await fetch(
                `http://127.0.0.1:8000/api/students/${this.student.id}/`,
                {
                    method: "put",
                    headers: {
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify(this.student),
                }
            );
            await this.getStudents();
            this.student = {};
        },
        async deleteStudent(student) {
            await this.getStudents();

            let response = await fetch(
                `http://127.0.0.1:8000/api/students/${student.id}/`,
                {
                    method: "delete",
                    headers: {
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify(this.student),
                }
            );
            await this.getStudents();
        },
    },
};
</script>
