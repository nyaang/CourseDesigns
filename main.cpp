#include "stdafx.h"
#include <iostream>
using namespace std;

//以十个人七项任务为例

typedef struct CTNODE {
	double cost; //存放个人经费消耗
	int person_num;	//记录是第几人的选择层，值等于当前结点所在层次数-1
	int task_num; //记录是第几个任务，值等于母结点的从左往右的第几个子结点数
	char* travellist[10];	//记录是遍历过哪些结点，遍历的时候会用上
	double allcost; //记录总的费用，遍历的时候会用上
	CTNODE* child[7]; //子结点
};

//初始化部分
void inittree(CTNODE& rootnode) {	//需要提供一个根节点的引用，和cost矩阵
	rootnode.cost = 0; rootnode.person_num = 0; rootnode.task_num = 0;	//根结点的数据成员无实际意义，全设为0
	//…利用cost矩阵给结点的cost赋值
}

//遍历算法函数部分
void traveltree(CTNODE& rootnode) {

}
//排序部分
void sortcost( ){

}

int main()
{hhh
	//system("pause");
	return 0;
}
