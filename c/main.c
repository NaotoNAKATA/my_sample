#include <stdio.h>

int main(int argc, char *argv[])
{
	FILE *fp;
	const char *filenme = argv[1];
	char c;
	const char str[] = "My Sample code\n";
	const char *p = str;

	if(argc!=2)
	{
		fprintf(stderr,"Not correct.\n");	
		return -1;
	}

	printf("Hello, my sample code\n");
	printf("Program = %s\n",argv[0]);

	/* File open(read) */
	if( (fp=fopen(filenme,"r"))==NULL )
	{
		fprintf(stderr,"File is not opened(read).\n");
		return -1;
	}

	/* File read */
	//while( (c=fgetc(fp)) !=EOF )
	//{
	//	printf("%c",c);
	//}
	char readline[256];
	while(fgets(readline, 256, fp)!=NULL) {
		printf("%s\n",readline);
	}

	fclose(fp);

	/* File open(write) */
	if( (fp=fopen("test.txt","w"))==NULL )
	{
		fprintf(stderr,"File is not opened(write).\n");
		return -1;
	}

	/* File write */
	while(*p!='\0')
	{
		fputc(*p++,fp);
	}

	fclose(fp);

	return 0;
}

