#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    char name[50];
    int points;
} Candidate;

void vote(Candidate candidates[], int candidate_count);
void save_results(Candidate candidates[], int candidate_count);
void load_results(Candidate candidates[], int candidate_count);
void display_results(Candidate candidates[], int candidate_count);

int main() {
    printf(" VOTING MACHINE");
    printf("\n");

    printf("\nChoose your candidate among David-Smith,Alexander-Johnson and Justin-Miller\n");
    printf("\n");

    Candidate candidates[] = {
        {"David-Smith", 0},
        {"Alexander-Johnson", 0},
        {"Justin-Miller", 0}
    };

    int candidate_count = sizeof(candidates) / sizeof(candidates[0]);

    load_results(candidates, candidate_count);
    vote(candidates, candidate_count);
    display_results(candidates, candidate_count);
    save_results(candidates, candidate_count);

    return 0;
}

void vote(Candidate candidates[], int candidate_count) {
    char vote_name[50];
    int vote_points;

    printf("Enter candidate's name: ");
    scanf("%s", vote_name);

    printf("Enter number of points: ");
    scanf("%d", &vote_points);

    for (int i = 0; i < candidate_count; i++) {
        if (strcmp(candidates[i].name, vote_name) == 0) {
            candidates[i].points += vote_points;
            break;
        }
    }
}

void save_results(Candidate candidates[], int candidate_count) {
    FILE *file;

    file = fopen("voting_results.txt", "w");

    if (file == NULL) {
        printf("Error opening file!\n");
        exit(1);
    }

    for (int i = 0; i < candidate_count; i++) {
        fprintf(file, "%s %d\n",
                candidates[i].name,
                candidates[i].points);
    }

    fclose(file);
}

void load_results(Candidate candidates[], int candidate_count) {
    FILE *file;
    char name[50];
    int points;

    file = fopen("voting_results.txt", "r");

    if (file == NULL) {
        printf("No previous results found.\n");
        return;
    }

    while (fscanf(file, "%s %d", name, &points) != EOF) {
        for (int i = 0; i < candidate_count; i++) {
            if (strcmp(candidates[i].name, name) == 0) {
                candidates[i].points = points;
                break;
            }
        }
    }

    fclose(file);
}

void display_results(Candidate candidates[], int candidate_count) {
    printf("\nVoting Results:\n");

    for (int i = 0; i < candidate_count; i++) {
        printf("%s: %d points\n",
               candidates[i].name,
               candidates[i].points);
    }
}